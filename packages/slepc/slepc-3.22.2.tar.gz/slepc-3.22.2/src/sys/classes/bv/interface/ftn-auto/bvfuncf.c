#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* bvfunc.c */
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

#include "slepcbv.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvdestroy_ BVDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvdestroy_ bvdestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreate_ BVCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreate_ bvcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreatefrommat_ BVCREATEFROMMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreatefrommat_ bvcreatefrommat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvinsertvec_ BVINSERTVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvinsertvec_ bvinsertvec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvinsertvecs_ BVINSERTVECS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvinsertvecs_ bvinsertvecs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvinsertconstraints_ BVINSERTCONSTRAINTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvinsertconstraints_ bvinsertconstraints
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetoptionsprefix_ BVSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetoptionsprefix_ bvsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvappendoptionsprefix_ BVAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvappendoptionsprefix_ bvappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetoptionsprefix_ BVGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetoptionsprefix_ bvgetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvview_ BVVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvview_ bvview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvviewfromoptions_ BVVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvviewfromoptions_ bvviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  bvdestroy_(BV *bv, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(bv);
 PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = BVDestroy(bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(bv);
 }
SLEPC_EXTERN void  bvcreate_(MPI_Fint * comm,BV *newbv, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(newbv);
 PetscBool newbv_null = !*(void**) newbv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newbv);
*ierr = BVCreate(
	MPI_Comm_f2c(*(comm)),newbv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newbv_null && !*(void**) newbv) * (void **) newbv = (void *)-2;
}
SLEPC_EXTERN void  bvcreatefrommat_(Mat A,BV *bv, int *ierr)
{
CHKFORTRANNULLOBJECT(A);
PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = BVCreateFromMat(
	(Mat)PetscToPointer((A) ),bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
}
SLEPC_EXTERN void  bvinsertvec_(BV V,PetscInt *j,Vec w, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(w);
*ierr = BVInsertVec(
	(BV)PetscToPointer((V) ),*j,
	(Vec)PetscToPointer((w) ));
}
SLEPC_EXTERN void  bvinsertvecs_(BV V,PetscInt *s,PetscInt *m,Vec *W,PetscBool *orth, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLINTEGER(m);
PetscBool W_null = !*(void**) W ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(W);
*ierr = BVInsertVecs(
	(BV)PetscToPointer((V) ),*s,m,W,*orth);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! W_null && !*(void**) W) * (void **) W = (void *)-2;
}
SLEPC_EXTERN void  bvinsertconstraints_(BV V,PetscInt *nc,Vec *C, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLINTEGER(nc);
PetscBool C_null = !*(void**) C ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(C);
*ierr = BVInsertConstraints(
	(BV)PetscToPointer((V) ),nc,C);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! C_null && !*(void**) C) * (void **) C = (void *)-2;
}
SLEPC_EXTERN void  bvsetoptionsprefix_(BV bv, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = BVSetOptionsPrefix(
	(BV)PetscToPointer((bv) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  bvappendoptionsprefix_(BV bv, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = BVAppendOptionsPrefix(
	(BV)PetscToPointer((bv) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  bvgetoptionsprefix_(BV bv, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
*ierr = BVGetOptionsPrefix(
	(BV)PetscToPointer((bv) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
SLEPC_EXTERN void  bvview_(BV bv,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(viewer);
*ierr = BVView(
	(BV)PetscToPointer((bv) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  bvviewfromoptions_(BV bv,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = BVViewFromOptions(
	(BV)PetscToPointer((bv) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
#if defined(__cplusplus)
}
#endif
