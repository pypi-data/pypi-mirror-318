#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* svdbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcsvd.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdcreate_ SVDCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdcreate_ svdcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdreset_ SVDRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdreset_ svdreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svddestroy_ SVDDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svddestroy_ svddestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsettype_ SVDSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsettype_ svdsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgettype_ SVDGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgettype_ svdgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetbv_ SVDSETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetbv_ svdsetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetbv_ SVDGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetbv_ svdgetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetds_ SVDSETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetds_ svdsetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetds_ SVDGETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetds_ svdgetds
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  svdcreate_(MPI_Fint * comm,SVD *outsvd, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outsvd);
 PetscBool outsvd_null = !*(void**) outsvd ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outsvd);
*ierr = SVDCreate(
	MPI_Comm_f2c(*(comm)),outsvd);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outsvd_null && !*(void**) outsvd) * (void **) outsvd = (void *)-2;
}
SLEPC_EXTERN void  svdreset_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDReset(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svddestroy_(SVD *svd, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(svd);
 PetscBool svd_null = !*(void**) svd ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDDestroy(svd);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! svd_null && !*(void**) svd) * (void **) svd = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(svd);
 }
SLEPC_EXTERN void  svdsettype_(SVD svd,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = SVDSetType(
	(SVD)PetscToPointer((svd) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  svdgettype_(SVD svd,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDGetType(
	(SVD)PetscToPointer((svd) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  svdsetbv_(SVD svd,BV V,BV U, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(U);
*ierr = SVDSetBV(
	(SVD)PetscToPointer((svd) ),
	(BV)PetscToPointer((V) ),
	(BV)PetscToPointer((U) ));
}
SLEPC_EXTERN void  svdgetbv_(SVD svd,BV *V,BV *U, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
PetscBool U_null = !*(void**) U ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(U);
*ierr = SVDGetBV(
	(SVD)PetscToPointer((svd) ),V,U);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! U_null && !*(void**) U) * (void **) U = (void *)-2;
}
SLEPC_EXTERN void  svdsetds_(SVD svd,DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(ds);
*ierr = SVDSetDS(
	(SVD)PetscToPointer((svd) ),
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  svdgetds_(SVD svd,DS *ds, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
PetscBool ds_null = !*(void**) ds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ds);
*ierr = SVDGetDS(
	(SVD)PetscToPointer((svd) ),ds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ds_null && !*(void**) ds) * (void **) ds = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
