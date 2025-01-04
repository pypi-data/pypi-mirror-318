#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* stsolve.c */
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

#include "slepcst.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stapply_ STAPPLY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stapply_ stapply
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stapplymat_ STAPPLYMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stapplymat_ stapplymat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stapplytranspose_ STAPPLYTRANSPOSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stapplytranspose_ stapplytranspose
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stapplyhermitiantranspose_ STAPPLYHERMITIANTRANSPOSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stapplyhermitiantranspose_ stapplyhermitiantranspose
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetbilinearform_ STGETBILINEARFORM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetbilinearform_ stgetbilinearform
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetoperator_ STGETOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetoperator_ stgetoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define strestoreoperator_ STRESTOREOPERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define strestoreoperator_ strestoreoperator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetup_ STSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetup_ stsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stpostsolve_ STPOSTSOLVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stpostsolve_ stpostsolve
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stbacktransform_ STBACKTRANSFORM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stbacktransform_ stbacktransform
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stisinjective_ STISINJECTIVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stisinjective_ stisinjective
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stmatsetup_ STMATSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stmatsetup_ stmatsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetworkvecs_ STSETWORKVECS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetworkvecs_ stsetworkvecs
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  stapply_(ST st,Vec x,Vec y, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(y);
*ierr = STApply(
	(ST)PetscToPointer((st) ),
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((y) ));
}
SLEPC_EXTERN void  stapplymat_(ST st,Mat X,Mat Y, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(X);
CHKFORTRANNULLOBJECT(Y);
*ierr = STApplyMat(
	(ST)PetscToPointer((st) ),
	(Mat)PetscToPointer((X) ),
	(Mat)PetscToPointer((Y) ));
}
SLEPC_EXTERN void  stapplytranspose_(ST st,Vec x,Vec y, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(y);
*ierr = STApplyTranspose(
	(ST)PetscToPointer((st) ),
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((y) ));
}
SLEPC_EXTERN void  stapplyhermitiantranspose_(ST st,Vec x,Vec y, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(y);
*ierr = STApplyHermitianTranspose(
	(ST)PetscToPointer((st) ),
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((y) ));
}
SLEPC_EXTERN void  stgetbilinearform_(ST st,Mat *B, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
*ierr = STGetBilinearForm(
	(ST)PetscToPointer((st) ),B);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
}
SLEPC_EXTERN void  stgetoperator_(ST st,Mat *Op, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool Op_null = !*(void**) Op ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Op);
*ierr = STGetOperator(
	(ST)PetscToPointer((st) ),Op);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Op_null && !*(void**) Op) * (void **) Op = (void *)-2;
}
SLEPC_EXTERN void  strestoreoperator_(ST st,Mat *Op, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool Op_null = !*(void**) Op ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Op);
*ierr = STRestoreOperator(
	(ST)PetscToPointer((st) ),Op);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Op_null && !*(void**) Op) * (void **) Op = (void *)-2;
}
SLEPC_EXTERN void  stsetup_(ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetUp(
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  stpostsolve_(ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STPostSolve(
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  stbacktransform_(ST st,PetscInt *n,PetscScalar* eigr,PetscScalar* eigi, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLSCALAR(eigr);
CHKFORTRANNULLSCALAR(eigi);
*ierr = STBackTransform(
	(ST)PetscToPointer((st) ),*n,eigr,eigi);
}
SLEPC_EXTERN void  stisinjective_(ST st,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STIsInjective(
	(ST)PetscToPointer((st) ),is);
}
SLEPC_EXTERN void  stmatsetup_(ST st,PetscScalar *sigma,PetscScalar *coeffs, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLSCALAR(coeffs);
*ierr = STMatSetUp(
	(ST)PetscToPointer((st) ),*sigma,coeffs);
}
SLEPC_EXTERN void  stsetworkvecs_(ST st,PetscInt *nw, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetWorkVecs(
	(ST)PetscToPointer((st) ),*nw);
}
#if defined(__cplusplus)
}
#endif
