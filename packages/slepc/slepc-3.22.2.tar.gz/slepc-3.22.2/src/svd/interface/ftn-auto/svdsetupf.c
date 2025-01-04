#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* svdsetup.c */
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
#define svdsetoperators_ SVDSETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetoperators_ svdsetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetoperators_ SVDGETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetoperators_ svdgetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetsignature_ SVDSETSIGNATURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetsignature_ svdsetsignature
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdgetsignature_ SVDGETSIGNATURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdgetsignature_ svdgetsignature
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetdstype_ SVDSETDSTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetdstype_ svdsetdstype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetup_ SVDSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetup_ svdsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdsetinitialspaces_ SVDSETINITIALSPACES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdsetinitialspaces_ svdsetinitialspaces
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define svdallocatesolution_ SVDALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define svdallocatesolution_ svdallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  svdsetoperators_(SVD svd,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = SVDSetOperators(
	(SVD)PetscToPointer((svd) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  svdgetoperators_(SVD svd,Mat *A,Mat *B, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
*ierr = SVDGetOperators(
	(SVD)PetscToPointer((svd) ),A,B);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
}
SLEPC_EXTERN void  svdsetsignature_(SVD svd,Vec omega, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(omega);
*ierr = SVDSetSignature(
	(SVD)PetscToPointer((svd) ),
	(Vec)PetscToPointer((omega) ));
}
SLEPC_EXTERN void  svdgetsignature_(SVD svd,Vec omega, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
CHKFORTRANNULLOBJECT(omega);
*ierr = SVDGetSignature(
	(SVD)PetscToPointer((svd) ),
	(Vec)PetscToPointer((omega) ));
}
SLEPC_EXTERN void  svdsetdstype_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetDSType(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svdsetup_(SVD svd, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDSetUp(
	(SVD)PetscToPointer((svd) ));
}
SLEPC_EXTERN void  svdsetinitialspaces_(SVD svd,PetscInt *nr,Vec isr[],PetscInt *nl,Vec isl[], int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
PetscBool isr_null = !*(void**) isr ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(isr);
PetscBool isl_null = !*(void**) isl ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(isl);
*ierr = SVDSetInitialSpaces(
	(SVD)PetscToPointer((svd) ),*nr,isr,*nl,isl);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! isr_null && !*(void**) isr) * (void **) isr = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! isl_null && !*(void**) isl) * (void **) isl = (void *)-2;
}
SLEPC_EXTERN void  svdallocatesolution_(SVD svd,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(svd);
*ierr = SVDAllocateSolution(
	(SVD)PetscToPointer((svd) ),*extra);
}
#if defined(__cplusplus)
}
#endif
